# SQL Migrations

This directory contains database migration scripts for schema evolution and versioning.

## Purpose

Database migrations track and manage changes to the database schema over time, allowing:
- Version control of schema changes
- Rollback to previous states
- Reproducible database setup across environments
- Clear history of modifications

## Structure

Migrations are organized by version:
- `001_initial_schema.sql` - Initial database structure
- `002_add_field.sql` - Feature additions
- `003_refactor.sql` - Schema reorganization

## Implementation

Migrations will be created during future modules to:
1. Track schema modifications
2. Add new tables or columns
3. Update constraints or indexes
4. Document database evolution

## Related Files

- Database schemas: `/sql/schemas/M1S8/`
- Create scripts: `/sql/schemas/M1S8/create_tables.sql`

## Course reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
