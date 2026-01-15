from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend import models, schemas
from backend.database import get_db

router = APIRouter(prefix="/artifacts", tags=["artifacts"])

# 创建新文物
@router.post("/", response_model=schemas.Artifact)
def create_artifact(artifact: schemas.ArtifactCreate, db: Session = Depends(get_db)):
    # 检查是否已存在相同ID
    db_artifact = db.query(models.Artifact).filter(models.Artifact.artifact_id == artifact.artifact_id).first()
    if db_artifact:
        raise HTTPException(status_code=400, detail="文物ID已存在")
    
    # 创建新文物记录
    db_artifact = models.Artifact(**artifact.dict())
    db.add(db_artifact)
    db.commit()
    db.refresh(db_artifact)
    return db_artifact

# 获取单个文物详情
@router.get("/{artifact_id}", response_model=schemas.Artifact)
def read_artifact(artifact_id: str, db: Session = Depends(get_db)):
    db_artifact = db.query(models.Artifact).filter(models.Artifact.artifact_id == artifact_id).first()
    if db_artifact is None:
        raise HTTPException(status_code=404, detail="文物未找到")
    return db_artifact

# 获取文物列表
@router.get("/", response_model=List[schemas.Artifact])
def read_artifacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    artifacts = db.query(models.Artifact).offset(skip).limit(limit).all()
    return artifacts
