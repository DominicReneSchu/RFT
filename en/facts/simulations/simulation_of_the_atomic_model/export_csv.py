import csv

def export_resonances(filename, resonance_history):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Resonanzzeitpunkt'])
        for t_res in resonance_history:
            writer.writerow([t_res])
    print(f"Resonanzereignisse exportiert nach {filename}")