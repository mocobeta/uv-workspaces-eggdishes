import pluggy

hookspec = pluggy.HookspecMarker("eggdishes")
hookimpl = pluggy.HookimplMarker("eggdishes")


@hookspec
def register_eggdish(recipes):
    """Register egg dish recipe."""
    pass