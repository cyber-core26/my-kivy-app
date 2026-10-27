import time
import threading

# 1. GLOBAL DATABASE (Follow status verification)
FOLLOWERS_DATABASE = {
    "party_a": {"party_b"},  # Party A follows Party B
    "party_b": {"party_a"},  # Party B follows Party A
    "party_c": {"party_a"}  # Party C follows Party A (One-way only)
}

USER_TAP_TRACKER = {}
ALERT_STATE = {"acknowledged": False}


def verify_mutual_relationship(user_sender, user_receiver):
    """Checks if both users explicitly follow each other."""
    sender_follows_receiver = user_receiver in FOLLOWERS_DATABASE.get(user_sender, set())
    receiver_follows_sender = user_sender in FOLLOWERS_DATABASE.get(user_receiver, set())
    return sender_follows_receiver and receiver_follows_sender


def trigger_hardware_escalation():
    """This runs if 'OK' was not input in time."""
    print("\n🚨 [ESCALATION SYSTEM ACTIVATED]")

    # 📝 CHANGE HERE: Put your real phone numbers here later!
    phone_numbers = ["+92354335426", "+92354890010"]

    for number in phone_numbers:
        print(f"--> OUTBOUND EMERGENCY PHONE CALL DIALED TO: {number}")


def start_ten_minute_timeout(alert_state_dict):
    """Runs a background countdown window without freezing the terminal."""
    print("\n⏳ [TIMER STARTED] Countdown running in background... Quick! You have 5 seconds to cancel!")

    # 📝 CHANGE HERE: Change 5 to 600 for a real 10-minute delay later!
    time.sleep(600)

    if not alert_state_dict.get("acknowledged", False):
        print("\n❌ [TIMEOUT EXPIRED] User failed to input OK within the window!")
        trigger_hardware_escalation()
    else:
        print("\n✅ [TIMER CANCELLED] Escalation averted. User input OK in time.")


def process_three_taps(username, target_receiver):
    """Enforces the strict 3-tap tracking rule."""
    current_time = time.time()

    if username not in USER_TAP_TRACKER:
        USER_TAP_TRACKER[username] = []

    USER_TAP_TRACKER[username].append(current_time)
    tap_count = len(USER_TAP_TRACKER[username])
    print(f"User [{username}] registered tap #{tap_count} targeting [{target_receiver}]")

    if tap_count == 3:
        USER_TAP_TRACKER[username] = []  # Reset counter immediately
        print(f"\n[3 TAPS DETECTED] Verifying connection between {username} and {target_receiver}...")

        if verify_mutual_relationship(username, target_receiver):
            print("✅ Verification Successful! Mutual relationship confirmed.")
            ALERT_STATE["acknowledged"] = False

            # Start background countdown thread
            timer_thread = threading.Thread(target=start_ten_minute_timeout, args=(ALERT_STATE,))
            timer_thread.start()
        else:
            print("❌ Verification Failed! No mutual connection found. Alert ignored.")


# =====================================================================
# PYCHARM LIVE INTERACTIVE TERMINAL TESTING
# =====================================================================
if __name__ == "__main__":
    print("--- SIMULATING 3 TAPS IN PYCHARM ---")

    test_sender = "party_a"
    test_receiver = "party_b"

    # Simulating 3 taps automatically to kick off the system
    process_three_taps(test_sender, test_receiver)
    process_three_taps(test_sender, test_receiver)
    process_three_taps(test_sender, test_receiver)

    # Live Interactive Input: Terminal will prompt you to type "OK"
    user_input = input("\n👉 Type 'OK' and press Enter immediately to cancel the alarm: ")