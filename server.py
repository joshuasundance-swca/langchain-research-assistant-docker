from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from research_assistant import chain as research_assistant_chain

app = FastAPI(
    title="LangChain Research Assistant",
)


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(app, research_assistant_chain, path="/research-assistant")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
