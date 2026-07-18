from core.security.migration import MemoryMigration

migration = MemoryMigration()


count = migration.migrate()


print("Migrated memories:", count)
