import heapq
from _collections import defaultdict
from bitarray import bitarray


def huffman(text: str):
    dt = defaultdict(int)
    for letter in text:
        dt[letter] += 1
    heap = [[freq, [key, ""]] for (key, freq) in dt.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        for pair in left[1:]:
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [right[0] + left[0]] + left[1:] + right[1:])
    huffman_list = left[1:] + right[1:]
    print(huffman_list)
    huffman_dict = {a[0]: bitarray(str(a[1])) for a in huffman_list}
    encoded_text = bitarray()
    encoded_text.encode(huffman_dict, text)
    return encoded_text


if __name__ == "__main__":
    print(huffman("123"))
