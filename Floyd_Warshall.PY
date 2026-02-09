class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        distance_matrix=[]
        for i in range(26):
            row=[]
            for j in range(26):
                if i==j:
                    row.append(0)
                else:
                    row.append(10**8)
            distance_matrix.append(row)

        for i in range(len(original)):
            original_char=original[i]
            changed_char=changed[i]
            changing_cost=cost[i]
            
            origin_index=ord(original_char)-ord('a')
            changes_index=ord(changed_char)-ord('a')

            if changing_cost<distance_matrix[origin_index][changes_index]:
                distance_matrix[origin_index][changes_index]=changing_cost

        for viva in range(26):
            for i in range(26):
                for j in range(26):
                    if distance_matrix[i][viva] != 10**8 and distance_matrix[viva][j] != 10**8:
                        distance_matrix[i][j]=min(distance_matrix[i][j],distance_matrix[i][viva]+distance_matrix[viva][j])

        total_cost = 0
        for char in range(len(source)):
            source_char=source[char]
            target_char=target[char]

            if source_char == target_char:
                continue
            
            source_number=ord(source_char)-ord('a')
            target_number=ord(target_char)-ord('a')
            if distance_matrix[source_number][target_number]==10**8:
                return -1

            total_cost+=distance_matrix[source_number][target_number]

        return total_cost