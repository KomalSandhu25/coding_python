import heapq
from heapq import _heapify_max


class AlternateStringPlacing:
    def reorganizeString( s: str) -> str:
        dictn = {}
        for val in s:
            if dictn.__contains__(val):
                c = dictn[val]
                dictn[val] = c+1
            else:
                dictn[val] = 1
        max_heap = [(f,c) for c, f in dictn.items()]
        _heapify_max(max_heap)
        res =[]
        print(max_heap)
        while len(max_heap) >= 2:
            freq1, val1 = heapq.heappop(max_heap)
            freq2, val2 = heapq.heappop(max_heap)

            res.extend([val1, val2])
            if int(freq1)-1 > 0:
                heapq.heappush(max_heap, (int(freq1)-1, val1))
            if int(freq2)-1 > 0:
                heapq.heappush(max_heap, (int(freq2)-1, val2))
            _heapify_max(max_heap)
        if max_heap:
            freq, val = heapq.heappop(max_heap)
            if int(freq) > 1:
                return ""
            res.append(val)
        return "".join(res)


if __name__=='__main__':
    print(AlternateStringPlacing.reorganizeString( "vvvlo"))
