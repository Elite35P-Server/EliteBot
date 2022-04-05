from db import async_session
import schemas, async_crud, models
import asyncio

async def test():
    ch = schemas.YouTubeCh(
        id='UC_x5XG1OV2P6uZZ5FSM9Ttw',
        name='YouTube',
        icon='',
        description='',
        subsc_count=0,
        play_count=0,
        video_count=0,
        #updated_at=,
        status='live',
    )
    async with async_session() as db:
        await async_crud.update_ytch(db, ch)
        data = await async_crud.get_ytch(db, 'UC_x5XG1OV2P6uZZ5FSM9Ttw')
        print(data)
        
if __name__ == '__main__':
    asyncio.run(test())