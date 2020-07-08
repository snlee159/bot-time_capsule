# Time Capsule
Time Capsule is a Slack bot which finds all pinned items in public channels and backs them up
to a Google doc.

## Run Instructions
Reach out to Sam Lee for the passwords file.

First time you run this, run for a full lookback with: 

`python3 -m time_capsule 1`

Every day after, run for the last 24 hours with: 

`python3 -m time_capsule`


## Output
A CSV with the pins from the last 24 hours

## Next Steps
- Change the output to save the new pins to a given shared Google doc rather than a CSV
- Add in some interactive functionality for users to search backed up pins