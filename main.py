import uuid
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI()

# In-memory "database"

