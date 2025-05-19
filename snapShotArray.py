"""
Snapshot Array - Medium

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.
Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 5 * 10**4
0 <= index < length
0 <= val <= 10**9
0 <= snap_id < (the total number of times we call snap())
At most 5 * 10**4 calls will be made to set, snap, and get.


Algorithm

-For each element nums[i] in the array, create an empty list to store its historical values, in the format of [snap_id, value]. Initialize each list by adding the first record [0, 0].

-Implement the set(index, val) method: add the historical record [snap_id, value] to the record list history_records[index].

-Implement the snap method: return snap_id and increment it by 1.

-Implement the get(index, snap_id) method to retrieve the value of nums[index] in the array with snapshot id as snap_id:

-Use binary search to find the rightmost insertion index of snapshot ID in the given version snap_index (so the target index is snap_index - 1).

Return history_records[index][snap_index - 1][1].
"""

import bisect

class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.history_records = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.history_records[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snap_index = bisect.bisect_right(self.history_records[index], [snap_id, 10 ** 9])
        return self.history_records[index][snap_index - 1][1]


class SnapshotArray_Out_Of_Memory:

    def __init__(self, length: int):
        self.length = length
        self.current_map = {}
        for i in range(length):
            self.current_map[i] = 0
        self.snapshots = {}
        self.snap_calls = 0
        
        

    def set(self, index: int, val: int) -> None:
        self.current_map[index] = val
        

    def snap(self) -> int:
        self.snapshots[self.snap_calls] = self.current_map.copy()
        self.snap_calls += 1
        return self.snap_calls -1
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]


if __name__ == "__main__":
    snapshotArr = SnapshotArray(3) # set the length to be 3
    snapshotArr.set(0,5) #  Set array[0] = 5
    print(snapshotArr.snap()) # Take a snapshot, return snap_id = 0
    snapshotArr.set(0,6)
    print(snapshotArr.get(0,0)) # Get the value of array[0] with snap_id = 0, return 5
    
    ## Test 2
    ##     ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
    ##      [[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
    ##      [null,null,0,1,2,15,3,4,15]
    snapshotArr = SnapshotArray(1)
    snapshotArr.set(0,15)
    snapshotArr.snap()
    snapshotArr.snap()
    snapshotArr.snap()
    print(snapshotArr.get(0,2)) # 15
    snapshotArr.snap()
    snapshotArr.snap()
    print(snapshotArr.get(0,0)) # 15

    