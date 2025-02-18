from fastapi import Header, HTTPException
from typing_extensions import Annotated

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != 'some-token':
        raise HTTPException(status_code=400, detail="X-Token header invalid")