## POC

# Fast API
uv run python -m grpc_tools.protoc -I./protos --python_out=./pb --grpc_python_out=./pb ./protos/application.proto

# Django
uv run python -m grpc_tools.protoc -I./greeting_services/protos --python_out=./greeting_services/pb --grpc_python_out=./greeting_services/pb ./greeting_services/protos/application.proto

# Development Mode
- Fastapi: uvicorn main:app --reload or uv run python main.py
- Django: uv run greeting_services/manage.py runserver 0:8001
