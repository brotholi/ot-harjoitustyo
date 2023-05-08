from database_connection import create_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        drop table if exists lihasloki_users; """)
    cursor.execute("""
        drop table if exists lihasloki_exercises; """)
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(("""
        create table lihasloki_users (
            username text primary key,
            password text
        );
        """))
    connection.commit()

    cursor.execute(("""    
        create table lihasloki_exercises (
            exercise_id primary key,
            logentry_id,
            name text,
            weight text,
            reps text
        );
        """))


def initialize_database():
    connection = create_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
