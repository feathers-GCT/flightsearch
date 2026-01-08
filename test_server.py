import asyncio
import json
from server import search_flights

async def main():
    print("Testing search_flights tool...")
    
    # Test parameters (default)
    try:
        result = await search_flights(
            trip_type="RT",
            departure_city="ICN",
            arrival_city="FUK",
            departure_date="2026-03-03",
            return_date="2026-03-09",
            adults=1,
            children=0,
            infants=0,
            seat_class="Y",
            raw_json=False
        )
        print("\n--- Summary Result ---")
        print(result)
        
        # Test raw_json
        print("\nTesting raw_json output...")
        raw_result = await search_flights(
            departure_city="ICN",
            arrival_city="FUK",
            raw_json=True
        )
        data = json.loads(raw_result)
        print(f"Success! Received {len(data.get('GoodsList', {}).get('Goods', []))} goods in raw JSON.")
        
    except Exception as e:
        print(f"Test failed with error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
