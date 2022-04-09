from db import async_session
import schemas, async_crud, models
import asyncio

async def test():
    async with async_session() as db:
        ch = schemas.YouTubeCh(
            id='UC_x5XG1OV2P6uZZ5FSM9Ttw',
            name='YouTube',
            icon='',
            description='',
            subsc_count=0,
            play_count=0,
            video_count=0,
            #updated_at=,
            status='none',
        )

        await async_crud.update_ytch(db, ch)
        data = await async_crud.get_ytch(db, 'UC_x5XG1OV2P6uZZ5FSM9Ttw')
        print(data)
            
        video = schemas.YouTubeVideo(
            ch_id='UC_x5XG1OV2P6uZZ5FSM9Ttw',
            id='test',
            title='test',
            thumbnails={},
            url='https://youtu.be/test',
            play_count=0,
            like_count=0,
            comment_count=0,
            status='none',
            current_viewers=None,
        )

        await async_crud.update_ytvideo(db, 'UC_x5XG1OV2P6uZZ5FSM9Ttw', video)
        data = await async_crud.get_ytvideos_date(db)
        print(data)

        
if __name__ == '__main__':
    asyncio.run(test())