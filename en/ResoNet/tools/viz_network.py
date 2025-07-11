"""
ResonanzNet Netzwerk-Visualisierung
Systemisch: Zeigt die Gruppenzugehörigkeit und Kopplung aller bekannten Knoten im Resonanzfeld.
"""

import json
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

CONFIG_PATH = Path("../setup/config.json")

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def build_network(node_name, peers):
    G = nx.Graph()
    G.add_node(node_name)
    for peer in peers:
        G.add_node(peer)
        G.add_edge(node_name, peer)
    return G

def visualize(G, node_name):
    plt.figure(figsize=(6,6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw_networkx_nodes(G, pos, node_color=["gold" if n==node_name else "skyblue" for n in G.nodes()])
    nx.draw_networkx_labels(G, pos, font_size=10)
    nx.draw_networkx_edges(G, pos)
    plt.title("ResonanzNet – Netzwerkstruktur")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

def main():
    config = load_config()
    node_name = config.get("node_name", "raspy.local")
    peers = config.get("peers", [])
    G = build_network(node_name, peers)
    visualize(G, node_name)

if __name__ == "__main__":
    main()