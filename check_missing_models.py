#!/usr/bin/env python3

import os
import json

def extract_missing_items_from_logs():
    """Extract all missing item names from the error pattern"""
    # From the logs, extract pattern: Unable to load model: 'mtsofficialpack:item/ITEMNAME'
    log_text = """
    mirrorornament_rubix fuzeproxy spraycan_black instrument_car_fuelqty merc230_salmon
    fordmustang69_bluestripe brigbedbox fordmustang69_white crashbarrier grilleornament_horns
    merc230_extravagant skyhawk_red vulcanair_orange instrument_car_electric sign_cow
    mc172_oak instrument_car_oilpressure_p brigbedtanker_greenred instrument_car_oilpressure_b
    brigbeddump_dirt merc230_brown repairkit enginequad brigbeddump_coal mirrorornament_blockacacia
    ocpbutter mirrorornament_pine comanche_blackred spotlight carseat_brown mirrorornament_1911gray
    dump_storage seatyellow spotlight_bell206 fluidunloader wheelsmall_legacy enginedetroitdiesel
    gunflaregun merc230_olive e500_blue hydraulics sign_noparking comanche_yellow dump_dropper
    pzl37los_brown skidhelicopter comanche_blackredstripe bullet3700proxy pole_crossingsignal
    paint_black bullet3700solid_mag vulcanair_cow beacon_tower_inverted crate_green watercannon
    barrel scout_red aa_turret_37 fordmustang69_lime carseat_black drill mirrorornament_saturn
    propellerrotor mirrorornament_blockgrass wheellarge_spokes2 gmcbrig_tan bell47g_blue
    extinguisherfoam carseat_red wheelsmall brigbedtanker_blank bullet3700he_mag spring
    pole_flashingsignal_red nuts skyhawk_blackred fordmustang69_seagreen fordmustang69_police
    merc230_blue fordmustang69_yellow grilleornament_snail enginemercedesm102 brigbeddump_moss
    mirrorornament_anvil crate_blue brigbeddump_copper vulcanair_green instrument_aircraft_flaps
    wheelmedium_legacy wheellarge_holering sign_turn_right pontoon bulletflare_red heavy_bomb
    wheellarge_whiterim comanche_orangebrown sign_priority mirrorornament_steak brigbeddump_nether
    fordmustang69_orange plating e500_green signalcontroller propellersmall2blade skyhawk_coffee
    bulletflare_white aa_base merc230_yellow fordmustang69_red sign_route sign_speedlimit
    vulcanair_yellow glovebox_skyhawk instrument_car_spedometer_kph trimotor_blue vulcanair_redsnail
    smallarmscartridge bulletrocket bulldozer_green bulldozer_blue bulldozer_sand dozerblade
    truck_yellow truck_silver truck_blue truck_red tank_m60 tank_t34_85 tank_t26e4
    tank_a10 tank_wiesel1a4 tank_leo2a4 tank_centurion tank_challenger2 tank_abrams
    tank_ariete tank_type90
    """

    # Extract all unique item names
    items = set()
    for word in log_text.split():
        if word and not word.startswith('#'):  # Skip comments
            items.add(word.strip())

    return sorted(list(items))

def main():
    """Check which models exist and which are still missing"""

    models_dir = "src/main/resources/assets/mtsofficialpack/models/item"

    # Get all items that should exist
    all_items = extract_missing_items_from_logs()

    existing_models = []
    missing_models = []

    for item_name in all_items:
        model_path = os.path.join(models_dir, f"{item_name}.json")
        if os.path.exists(model_path):
            existing_models.append(item_name)
        else:
            missing_models.append(item_name)

    print(f"EXISTING MODELS ({len(existing_models)}):")
    for item in existing_models:
        print(f"  + {item}")

    print(f"\nMISSING MODELS ({len(missing_models)}):")
    for item in missing_models:
        print(f"  - {item}")

    print(f"\nSUMMARY:")
    print(f"Total items: {len(all_items)}")
    print(f"Existing: {len(existing_models)}")
    print(f"Missing: {len(missing_models)}")

    # Check specific items that user mentioned are still problems
    problem_items = ["gunflaregun", "confetti"]  # confetti might be different name
    print(f"\nChecking specific problem items:")
    for item in problem_items:
        model_path = os.path.join(models_dir, f"{item}.json")
        if os.path.exists(model_path):
            print(f"  + {item} - model exists")
        else:
            print(f"  - {item} - NO MODEL FOUND")

if __name__ == "__main__":
    main()