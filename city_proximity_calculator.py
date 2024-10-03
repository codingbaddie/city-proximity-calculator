import pandas as pd
from geopy.distance import geodesic
from tqdm import tqdm

def calculate_distances(df):
    results = []
    for i, city in tqdm(df.iterrows(), total=len(df)):
        distances = []
        for j, other_city in df.iterrows():
            if i != j:
                dist = geodesic((city['latitude'], city['longitude']), 
                                 (other_city['latitude'], other_city['longitude'])).km
                distances.append((other_city['l3_city'], dist))
        
        nearest = sorted(distances, key=lambda x: x[1])[:3]
        results.append({
            'Province': city['l2_province'],
            'city ID': city['l3_city_id'],
            'city': city['l3_city'],
            'nearby 1': nearest[0][0] if len(nearest) > 0 else '',
            'nearby 2': nearest[1][0] if len(nearest) > 1 else '',
            'nearby 3': nearest[2][0] if len(nearest) > 2 else ''
        })
    return results

def main():
    # Read the CSV file
    df = pd.read_csv('List of ID Cities - Sheet1.csv')
    
    # Ensure latitude and longitude columns are float
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    
    # Remove rows with NaN latitude or longitude
    df = df.dropna(subset=['latitude', 'longitude'])
    
    # Calculate distances
    results = calculate_distances(df)
    
    # Create a DataFrame from results
    results_df = pd.DataFrame(results)
    
    # Save results to CSV file
    results_df.to_csv('nearest_cities_results.csv', index=False)
    
    print("Results have been saved to nearest_cities_results.csv file.")

if __name__ == "__main__":
    main()