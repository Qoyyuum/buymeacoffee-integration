# Introduction

BuyMeACoffee has webhooks to signal events happening on a person's/org's BuyMeACoffee page. This repo just takes those signal events and saves them to Supabase.

:construction: This is a Work In Progress. But essentially the goal is to have this as a deployable web service to capture online payments and signal an online service of its status.

# Build and Development

This project is built with Pipenv.

```shell
pip install pipenv
pipenv install
```

Then either enter the pipenv shell and run the application (via Uvicorn)

```shell
pipenv shell
uvicorn main:app --reload
```

Or run outside of it:

```shell
pipenv run uvicorn main:app --reload
```