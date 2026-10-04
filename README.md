## Cache & Idempotency Test

This section demonstrates MergeMind's diff caching behavior.

The same code changes should not be sent to the AI repeatedly when their
content has already been reviewed.

Test scenario:

1. Existing files in this PR were already reviewed.
2. This README was modified in a later commit.
3. MergeMind receives the updated pull-request webhook.
4. Previously reviewed unchanged diffs should produce cache hits.
5. Only newly changed content should require additional processing.

This helps reduce unnecessary AI API calls and improves review efficiency.