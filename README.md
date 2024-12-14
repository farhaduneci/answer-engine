# AI Answer Engine

This is a simple answer engine test project leveraging [PydanticAI](https://ai.pydantic.dev) for educational purposes.

Pydantic AI agent answers questions using the search tool provided to it to search the web using [Tavily](https://tavily.com) and infer the answer by [Groq](https://groq.com) models.

## 🚀 Usage

1. Rename `.env.example` file to `.env` in the root directory and set the environment variables.

2. Run the FastAPI application:
    ```sh
    uvicorn app.api:main --reload
    ```
3. You can now access the API at `http://127.0.0.1:8000/search`.

> Sample API collections are available in the `docs` directory. you can view and work with them using [Bruno](https://www.usebruno.com).

## 🔎 Example

```sh
curl -X 'POST' \
  'http://127.0.0.1:8000/search' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "query": "How's the weather like today in Tehran?"
    }'
```

```json
{
    "answer": "The weather in Tehran today is partly cloudy with a temperature of -2.7°C. The wind is coming from the north-northwest at a speed of 14.0 kph, and the humidity is at 58%. The conditions make it feel like -7.5°C. There is no precipitation, and the visibility is about 10 kilometers."
}
```

## 📄 License

This project is licensed under the MIT License.
