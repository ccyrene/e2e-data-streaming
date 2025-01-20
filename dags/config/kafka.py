class KafkaConfig:
    def __init__(self, bootstrap_servers, max_block_ms=1000):
        self.bootstrap_servers = [bootstrap_servers]
        self.max_block_ms = max_block_ms

    def __repr__(self):
        return f"KafkaConfig(bootstrap_servers={self.bootstrap_servers}"
    
    def to_dict(self):
        return {
            "bootstrap_servers": self.bootstrap_servers,
            "max_block_ms": self.max_block_ms
        }