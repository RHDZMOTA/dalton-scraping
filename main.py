from service.scraping import Dalton
from service.database import Postgresql


def main():
    # Create service instances
    dalton = Dalton()
    database = Postgresql()

    # Save models
    for model in dalton.models:
        database.add(model)
        database.add_many(model.colors)
        database.add_many(model.versions)
        database.commit()

    # Close database connection
    database.close()


if __name__ == "__main__":
    main()
