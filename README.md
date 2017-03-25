# Intro-Hadoop-MapReduce

Analyze discussion forum data with Hadoop and MapReduce

Useful field names:
--------------------
**final_project:**

"forum_node.tsv"
"id"    "title" "tagnames"      "author_id"     "body"  "node_type"     "parent_id"     "abs_parent_id" "added_at"      "score" "state_string"  "last_edited_id"        "last_activity_by_id"   "last_activity_at"      "active_revision_id"    "extra" "extra_ref_id"  "extra_count"   "marked"

"forum_users.tsv"
"user_ptr_id"   "reputation"    "gold"  "silver"        "bronze"


**Analyzing Reddit comments:**

- subreddit: The subreddit the comment was posted in
- author: Username of the comment author
- body: Comment text
- create_utc: UTC timestamp of when the comment was posted
- ups: Comment upvotes
- downs: Comment downvotes
- gilded: 1 if the user was given Reddit gold for the comment, 0 otherwise
- archived: 1 if the comment was archived, 0 otherwise
