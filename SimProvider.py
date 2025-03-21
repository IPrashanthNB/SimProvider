class SIMCard:

    """Represents a SIM card with basic functionalities."""
    def __init__(self, sim_id, provider, balance=0):
        self.sim_id = sim_id
        self.provider = provider
        self.balance = balance
        self.active = True

    def recharge(self, amount):
        """Recharge the SIM card with the given amount."""
        if self.active:
            self.balance += amount
            print(f"Recharged {amount}. New balance: {self.balance}")
        else:
            print("Cannot recharge inactive SIM.")

    def make_call(self, minutes):
        """Simulate a phone call and deduct the cost from the balance."""
        cost = minutes * 2  # Assume 2 units/minute call rate
        if self.active and self.balance >= cost:
            self.balance -= cost
            print(f"Call made for {minutes} minutes. Remaining balance: {self.balance}")
        elif not self.active:
            print("Cannot make call on inactive SIM.")
        else:
            print("Insufficient balance.")

    def deactivate(self):
        """Deactivate the SIM card."""
        self.active = False
        print(f"SIM {self.sim_id} has been deactivated.")

    def activate(self):
        """Activate the SIM card."""
        self.active = True
        print(f"SIM {self.sim_id} has been activated.")

    def display_info(self):
        """Display SIM card details."""
        status = "Active" if self.active else "Inactive"
        print(f"SIM ID: {self.sim_id}\nProvider: {self.provider}\nBalance: {self.balance}\nStatus: {status}")

class SIMProvider:
    """Represents a SIM provider managing multiple SIM cards."""
    def __init__(self, name):
        self.name = name
        self.sim_cards = {}

    def create_sim(self, sim_id):
        """Create a new SIM card under this provider."""
        if sim_id not in self.sim_cards:
            sim = SIMCard(sim_id, self.name)
            self.sim_cards[sim_id] = sim
            print(f"SIM {sim_id} created under {self.name}.")
        else:
            print(f"SIM {sim_id} already exists.")

    def list_sims(self):
        """List all SIM cards managed by the provider."""
        print(f"SIMs under {self.name}:")
        for sim_id, sim in self.sim_cards.items():
            print(f" - {sim_id}: {sim.provider}, Balance: {sim.balance}, Status: {'Active' if sim.active else 'Inactive'}")

    def get_sim(self, sim_id):
        """Retrieve a SIM card by its ID."""
        return self.sim_cards.get(sim_id, None)

def main():
    """Main program logic for SIM management."""
    provider = SIMProvider("AirTel")  # Create a SIM provider
    provider.create_sim("12345")       # Add a SIM card
    provider.create_sim("67890")       # Add another SIM card

    sim1 = provider.get_sim("12345")
    sim2 = provider.get_sim("67890")

    if sim1:
        sim1.recharge(100)
        sim1.make_call(20)
        sim1.display_info()

    if sim2:
        sim2.recharge(50)
        sim2.make_call(10)
        sim2.deactivate()
        sim2.display_info()

    provider.list_sims()  # List all SIM cards

if __name__ == "__main__":
    main()

