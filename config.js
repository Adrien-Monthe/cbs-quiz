// =========================================================
// CBS Quiz - Shared Leaderboard configuration
// =========================================================
//
// Pick ONE option below and fill it in. Leave the others empty.
// If you leave them all empty, the app falls back to local-only
// (each browser sees only its own scores). The quiz still works.
//
// ---------------------------------------------------------
// OPTION A — Firebase Realtime Database  (RECOMMENDED — most reliable)
// ---------------------------------------------------------
// Setup (~5 min, free):
//   1. Go to https://console.firebase.google.com and sign in with Google.
//   2. Click "Add project" -> any name -> skip Analytics -> Create.
//   3. In the left sidebar click "Build" -> "Realtime Database".
//   4. Click "Create Database" -> pick any location -> choose
//      "Start in test mode" (allows public read/write — fine for a quiz app).
//      Click Enable.
//   5. At the top of the database page you'll see a URL like:
//          https://your-project-default-rtdb.firebaseio.com
//      Copy that URL (no trailing slash) and paste it below.
//
// Test-mode rules expire in 30 days. To keep it open longer, go to
// the "Rules" tab and set:
//      { "rules": { ".read": true, ".write": true } }
// then click Publish. Or set time-limited rules for stricter security.
//
// ---------------------------------------------------------
// OPTION B — Pantry  (SIMPLEST — no Google account needed)
// ---------------------------------------------------------
// Setup (~2 min, free):
//   1. Go to https://getpantry.cloud and enter any email.
//   2. They'll create a Pantry and show you a Pantry ID
//      (a UUID like 12345678-90ab-cdef-1234-567890abcdef).
//   3. Copy the Pantry ID and paste it below.
// That's it — no API key, no console, nothing else to configure.
//
// =========================================================

const CONFIG = {
  // OPTION A — Firebase Realtime Database URL (no trailing slash)
  FIREBASE_URL: "",   // e.g. "https://cbs-quiz-default-rtdb.firebaseio.com"

  // OPTION B — Pantry ID (UUID from getpantry.cloud)
  PANTRY_ID:    "ebdbac36-21fe-4efa-8c56-6be4207880c8",   // e.g. "12345678-90ab-cdef-1234-567890abcdef"
};
