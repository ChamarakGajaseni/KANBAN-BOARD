# KANBAN BOARD



## Installation

[Installation]()

## Running the Application

Option #1 Running : run by typing this code in your terminal, cmd or powershell.
- Run backend (use different terminals for each)
```
cd services/user_service
uvicorn main:app --reload --port 8001


cd services/board_service
uvicorn main:app --reload --port 8002


cd services/notification_service
uvicorn main:app --reload --port 8003
```

Option #2 Running : Using a shell script

```
#!/bin/bash

# Run all services at once
echo "Starting User Service..."
(cd services/user_service && uvicorn main:app --reload --port 8001) &

echo "Starting Board Service..."
(cd services/board_service && uvicorn main:app --reload --port 8002) &

echo "Starting Notification Service..."
(cd services/notification_service && uvicorn main:app --reload --port 8003) &

```

- Run frontend
```
npm install
npm start
```

** Please make sure that your path is in the KANBAN-BOARD directory.

## Setting Up Social Applications

## Demo Admin

## Demo Users
| Username | Password |
| -------- | ------- |
| test@example.com | 123456 |
