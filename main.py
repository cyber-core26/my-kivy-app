# main.py
import threading
import config
import logic as system_logic  # 'logic' ko rename kiya taake PyCharm ka Literal error khatam ho


def share_live_location():
    """Action 1: Tracks GPS coordinates and broadcasts live location mapping updates."""
    print("\n📍 [ACTION 1: LOCATION SHARING ACTIVATED]")
    print("--> Fetching exact GPS coordinates (Latitude/Longitude)...")
    print("--> Broadcasting secure live-tracking maps link to emergency contacts.")


def start_voice_recording():
    """Action 2: Accesses the microphone interface to record ambient environmental audio."""
    print("\n🎙️ [ACTION 2: AUDIO RECORDING STARTED]")
    print("--> Microphone hardware active. Saving ambient audio logs safely to device.")


def trigger_hardware_escalation():
    """Action 3: Loops through the phone array to place direct outbound phone calls."""
    print("\n📞 [ACTION 3: OUTBOUND EMERGENCY PHONE CALL GENERATION]")
    my_emergency_numbers=["+92334263015,+92354890010"]
    for number in config.ESCALATION_PHONE_NUMBERS:
        print(f"--> DIALING IMMEDIATE EMERGENCY CALL TO: {number}")


def receive_emergency_notification(sender_name, receiver_name):
    """
    Fires IMMEDIATELY when emergency conditions (3 taps) pass.
    """
    print(f"\n💥 [ALERT] Triggered by user: {sender_name}")

    # -----------------------------------------------------------------
    # THE 3 INPUT ACTIONS TRIGGER IMMEDIATELY HERE ON THE 3RD TAP
    # -----------------------------------------------------------------
    share_live_location()
    start_voice_recording()
    trigger_hardware_escalation()

    # -----------------------------------------------------------------
    # AFTER THE ACTIONS: Show the screen panels and run the background window
    # -----------------------------------------------------------------
    print(f"\n=== SCREEN ALERT ON {receiver_name.upper()}'S PHONE ===")
    print(f"Theme Background Color Applied: {config.APP_THEME_COLOR}")
    print(f"Display Message: {config.NOTIFICATION_TEXT}")
    print("[HARDWARE ACTUATOR] Command sent: >>> VIBRATE PHONE MOTOR CONSTANTLY <<<")

    # Track acknowledgement state safely across background threads
    alert_status = {"acknowledged": False}

    # Launch background countdown timer tracker
    timer_thread = threading.Thread(target=system_logic.start_ten_minute_timeout, args=(alert_status,))
    timer_thread.start()

    # Simulating UI Interactive button response options
    user_input = input("\nPress 'K' and hit Enter to simulate clicking 'OK' on screen: ")
    if user_input.lower() == 'k':
        alert_status["acknowledged"] = True
        print("[SYSTEM LOG] Acknowledgement received successfully.")


def simulate_screen_tap(user_profile, recipient_profile):
    """
    Simulates a hardware screen touch coordinate event hook.
    """
    # First, verify if both entities are permitted to communicate via mutual follow loop
    if not system_logic.verify_mutual_relationship(user_profile, recipient_profile):
        print(f"Operation Denied: {user_profile} and {recipient_profile} do not follow each other.")
        return

    is_emergency_triggered = system_logic.process_three_taps(user_profile)

    if is_emergency_triggered:
        print(f"\n[SUCCESS] Exactly 3 taps confirmed for {user_profile}!")
        receive_emergency_notification(user_profile, recipient_profile)


if __name__ == "__main__":
    print(f"Starting {config.ESCALATION_PHONE_NUMBERS} Core Engine...")

    # Simulating Party A tapping exactly 3 times
    simulate_screen_tap("party_a", "party_b")
    simulate_screen_tap("party_a", "party_b")
    simulate_screen_tap("party_a", "party_b")