// =========================================================
// CBS Quiz - Leaderboard configuration
// =========================================================
//
// LEAVE EMPTY for local-only leaderboard (each browser sees its own scores).
// FILL IN to enable a global shared leaderboard (all players see everyone).
//
// Quick setup (5 minutes, FREE):
//   1. Go to https://jsonbin.io and sign up (free).
//   2. Click "API Keys" in the sidebar -> copy your X-MASTER-KEY.
//   3. Click "Bins" -> "Create Bin" -> paste this JSON:
//          { "scores": [] }
//      Click "Create".
//   4. From the bin URL, copy the BIN ID (the long string after /b/).
//   5. Paste both below.
//
// Security note: the master key here is exposed in your public repo.
// JSONBin lets you create a separate "Access Key" with PUT permission
// only for that specific bin — recommended for production use. For a
// personal study app this is fine.
// =========================================================

const CONFIG = {
  JSONBIN_KEY:    "",   // e.g. "$2a$10$abc123..."
  JSONBIN_BIN_ID: "",   // e.g. "65f1a2b3c4d5e6f7..."
};
