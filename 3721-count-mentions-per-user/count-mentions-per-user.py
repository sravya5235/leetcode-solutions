from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        """
        Simulation approach.
        Time: O(E * U + total_id_tokens) where E = len(events), U = numberOfUsers
        Space: O(U)
        """
        # Convert timestamp strings to ints and sort by (timestamp, type)
        # Tie-breaker: OFFLINE should be processed before MESSAGE at same timestamp.
        def key_fn(ev):
            typ, t, _ = ev
            t = int(t)
            order = 0 if typ == "OFFLINE" else 1
            return (t, order)
        
        events_sorted = sorted(events, key=key_fn)
        
        mentions = [0] * numberOfUsers
        # offline_end[i] = timestamp when user i becomes online again
        # user is online at time t iff t >= offline_end[i]
        offline_end = [0] * numberOfUsers  # initially all online (timestamps >=1)
        
        for typ, ts, payload in events_sorted:
            t = int(ts)
            if typ == "OFFLINE":
                uid = int(payload)
                # user guaranteed to be online at this timestamp per constraints
                offline_end[uid] = t + 60
            else:  # MESSAGE
                tokens = payload.split()
                # handle tokens; tokens are either "ALL", "HERE", or a sequence of idX tokens
                # The problem states the mentions_string can contain either tokens id<number> (multiple),
                # or ALL, or HERE — but to be safe handle combinations as well.
                # If "ALL" present ---> increment all users by number of occurrences of "ALL" (usually 1)
                # If "HERE" present ---> increment all currently online users by occurrences of "HERE"
                # For id<number> tokens, parse and increment for each occurrence.
                
                # Count occurrences for each token type
                for tok in tokens:
                    if tok == "ALL":
                        for i in range(numberOfUsers):
                            mentions[i] += 1
                    elif tok == "HERE":
                        for i in range(numberOfUsers):
                            if t >= offline_end[i]:
                                mentions[i] += 1
                    elif tok.startswith("id"):
                        # parse number after "id"
                        uid = int(tok[2:])
                        mentions[uid] += 1
                    else:
                        # ignore/unexpected token (not expected by constraints)
                        continue
        return mentions
