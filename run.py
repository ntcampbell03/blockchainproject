from coin import app
from gossip.gossip_main import main as run_gossip
    
if __name__ == "__main__":
    run_gossip()
    app.run(host='0.0.0.0', port=80)
    
