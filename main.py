from random import randint


class Agent:
    """Agent that can share their public key with another agent to compute a shared secret, without sharing that secret."""

    def __init__(self, name: str, prime: int = 2**4423 - 1, base: int = 2**17 - 1) -> None:
        self.name = name
        self.prime = prime
        self.base = base
        self.privkey = self.generate_private_key()
        self.pubkey = self.generate_public_key()
        self.sharedkey = None

    def generate_private_key(self) -> int:
        return randint(int(1e5), int(1e9 - 1))

    def generate_public_key(self) -> int:
        return pow(self.base, self.privkey, self.prime)

    def compute_shared_key(self, other_pubkey: int) -> None:
        self.sharedkey = pow(other_pubkey, self.privkey, self.prime)

    def __repr__(self) -> str:
        out = f"\n[ Agent: {self.name} ]"
        out += f"\n   Prime: {self.prime}"
        out += f"\n   Base: {self.base}"
        out += f"\n🔐 Private key: {self.privkey}"
        out += f"\n🔑 Public key: {self.pubkey}"
        if self.sharedkey is not None:
            out += f"\n🗝️  Shared key: {self.sharedkey}"
        return out + "\n"


def main():
    print("Creating Alice and Bob.")
    alice = Agent("Alice")
    bob = Agent("Bob")

    print("\nHere they are:")
    print(alice)
    print(bob)

    print("\nSharing pubkeys")
    print("- Alice -> Bob")
    bob.compute_shared_key(alice.pubkey)
    print("- Bob -> Alice")
    alice.compute_shared_key(bob.pubkey)

    print("\nNow they both have the same shared key!")
    print(alice)
    print(bob)

    assert alice.sharedkey == bob.sharedkey


if __name__ == "__main__":
    main()
