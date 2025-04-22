import guru.line
import guru.neck_line
from base_engine import BaseEngine


def hit(base_engine: BaseEngine) -> str:
    tags = [line.hit(base_engine), neck_line.hit(base_engine)]
    return ','.join([tag for tag in tags if tag])
