import lightbulb
import secret
import hikari
from pathlib import Path

class L_Drago(lightbulb.Bot):
    def __init__(self, token):#self, token: str, *, prefix: typing.Optional[prefix_T] = None, insensitive_commands: bool = False, ignore_bots: bool = True, owner_ids: typing.Iterable[int] = ..., help_class: typing.Type[help_.HelpCommand] = ..., delete_unbound_slash_commands: bool = True, recreate_changed_slash_commands: bool = True, slash_commands_only: bool = False, default_enabled_guilds: typing.Optional[typing.Union[int, typing.Iterable[int]]] = None, **kwargs: hikari.UndefinedType) -> None:
        self._token = token
        super().__init__(token=secret.token, prefix='1')#token, prefix=prefix, insensitive_commands=insensitive_commands, ignore_bots=ignore_bots, owner_ids=owner_ids, help_class=help_class, delete_unbound_slash_commands=delete_unbound_slash_commands, recreate_changed_slash_commands=recreate_changed_slash_commands, slash_commands_only=slash_commands_only, default_enabled_guilds=default_enabled_guilds, **kwargs)

    
L_Drago(token=secret.token)

