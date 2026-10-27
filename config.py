import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock


class SafetyApp(BoxLayout):
    def __init__(self, **kwargs):
        super(SafetyApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # 📄 CONFIGURATION INPUTS DIRECTLY INSIDE CODE
        self.emergency_numbers = ["+923001234567", "+923211234567"]  # Apne numbers yahan badlein
        self.timer_duration = 5.0  # Testing ke liye 5 seconds (Real deployment ke liye 600.0 kar dein)

        # UI Screen Label
        self.status_label = Label(
            text="🚨 Emergency Safety System Ready.\nTap the screen button 3 times.",
            font_size='18sp',
            halign='center'
        )
        self.add_widget(self.status_label)

        # Main Trigger Button (Simulates Tap Action)
        self.trigger_btn = Button(
            text="TAP SCREEN",
            background_color=(0.2, 0.6, 1, 1),
            font_size='22sp'
        )
        self.trigger_btn.bind(on_press=self.process_three_taps)
        self.add_widget(self.trigger_btn)

        # Acknowledge (OK) Button
        self.ok_btn = Button(
            text="Acknowledge (OK)",
            background_color=(0.2, 0.8, 0.2, 1),
            font_size='20sp',
            disabled=True
        )
        self.ok_btn.bind(on_press=self.handle_ok_press)
        self.add_widget(self.ok_btn)

        # System variables
        self.tap_tracker = []
        self.timeout_event = None
        self.alert_active = False

    # 🛠️ THE 3 INPUT SAFETY ACTIONS (Runs instantly on 3rd tap)
    def share_live_location(self):
        print("\n📍 [ACTION 1: LOCATION SHARING ACTIVATED]")
        self.status_label.text += "\n📍 Location sent to emergency contacts!"

    def start_voice_recording(self):
        print("\n🎙️ [ACTION 2: AUDIO RECORDING STARTED]")
        self.status_label.text += "\n🎙️ Microphone Recording Active!"

    def trigger_hardware_calls(self):
        print("\n📞 [ACTION 3: CALLS INITIATED]")
        for number in self.emergency_numbers:
            print(f"--> DIALING IMMEDIATE EMERGENCY CALL TO: {number}")

    # ⚡ 3-TAP LOGIC MONITOR
    def process_three_taps(self, *args):
        current_time = time.time()
        self.tap_tracker.append(current_time)
        tap_count = len(self.tap_tracker)

        self.status_label.text = f"Registered tap #{tap_count}"

        if tap_count == 3:
            self.tap_tracker = []  # Reset tracker
            self.trigger_emergency_protocol()

    def trigger_emergency_protocol(self):
        self.alert_active = True
        self.ok_btn.disabled = False
        self.status_label.text = "💥 EMERGENCY MATCHED!\n"

        # Fire 3 Actions instantly on 3rd tap
        self.share_live_location()
        self.start_voice_recording()
        self.trigger_hardware_calls()

        # Start Kivy Background Countdown Timer (No freeze!)
        self.timeout_event = Clock.schedule_once(self.start_timeout_escalation, self.timer_duration)

    def handle_ok_press(self, *args):
        if self.alert_active:
            if self.timeout_event:
                Clock.unschedule(self.timeout_event)  # Cancel background timer
            self.alert_active = False
            self.ok_btn.disabled = True
            self.status_label.text = "✅ Escalation Averted.\nUser clicked OK in time."

    def start_timeout_escalation(self, *args):
        self.ok_btn.disabled = True
        self.alert_active = False
        self.status_label.text = "🚨 TIMEOUT EXPIRED!\nBackup Emergency Protocols Sent."
        print("\n❌ [TIMEOUT EXPIRED] Backup alert triggered!")


class MainApp(App):
    def build(self):
        return SafetyApp()


def ESCALATION_PHONE_NUMBERS():
    return None


def APP_THEME_COLOR():
    return None