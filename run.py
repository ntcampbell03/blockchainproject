from coin import app
from gossip.gossip_main import main as run_gossip
from examples.connections_simulation import Simulation

if __name__ == "__main__":
    run_gossip()
    app.run(host='0.0.0.0', port=80)
    sim = Simulation(number_clients=30, number_connections_per_client=5)
    sim.run()
