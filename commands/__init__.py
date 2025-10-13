from .join import JoinCommand
from .leave import LeaveCommand
from .link import LinkCommand 
from .play import PlayCommand 
from .stop import StopCommand 
from .add import AddCommand 
from .queue import QueueCommand 
from .skip import SkipCommand 
from .back import BackCommand 


async def setup(bot):
    await bot.add_cog(JoinCommand(bot))
    await bot.add_cog(LeaveCommand(bot))
    await bot.add_cog(LinkCommand(bot))
    await bot.add_cog(PlayCommand(bot))
    await bot.add_cog(StopCommand(bot))
    await bot.add_cog(AddCommand(bot))
    await bot.add_cog(QueueCommand(bot))
    await bot.add_cog(SkipCommand(bot))
    await bot.add_cog(BackCommand(bot))