import pynecone as pc

class PynecrudConfig(pc.Config):
    pass

config = PynecrudConfig(
    app_name="pynecrud",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
