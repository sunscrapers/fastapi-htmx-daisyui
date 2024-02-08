import asyncio
from typing import List

from faker import Faker
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert

from app.dependencies.db import sessionmanager
from app.models.funfact import FunFact

fake = Faker()


async def bootstrap_data(session, num_facts: int = 10):
    print("Starting creating fake Fun Facts")
    fun_facts: List[dict] = []

    counter: int = 0
    for _ in range(num_facts):
        fun_fact = {
            "title": fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
            "description": fake.paragraph(nb_sentences=10, variable_nb_sentences=True, ext_word_list=None),
        }
        fun_facts.append(fun_fact)

        counter += 1
        if counter >= 10000:
            insert_stmt = insert(FunFact).values(fun_facts).on_conflict_do_nothing()
            await session.execute(insert_stmt)
            await session.commit()

            fun_facts = []
            counter = 0

    if fun_facts:
        insert_stmt = insert(FunFact).values(fun_facts).on_conflict_do_nothing()
        await session.execute(insert_stmt)
        await session.commit()
    # Get current count from database
    result = await session.execute(select(func.count(FunFact.id)))
    count = result.scalar_one()
    print(f"{count} Fun facts in database")


async def main():
    async with sessionmanager.session() as session:
        await bootstrap_data(session, num_facts=1000000)


if __name__ == "__main__":
    asyncio.run(main())
