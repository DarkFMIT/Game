all_plates = [[0 for i in range(80)] for j in range(80)]

water_coords = [
    [61, 63], [62, 62], [62, 60], [61, 61], [60, 62], [59, 63], [57, 63], [58, 62], [59, 61], [60, 60], [61, 59], [62, 58], [62, 56], [61, 57], [60, 58], [59, 59], [57, 61], [56, 62], [55, 63], [53, 63], [54, 62], [55, 61], [56, 60], [58, 58], [60, 56], [61, 55], [62, 54], [62, 52], [61, 53], [60, 54], [59, 55], [55, 59], [54, 60], [53, 61], [52, 62], [51, 63], [49, 63], [50, 62], [51, 61], [52, 60], [53, 59], [54, 58], [55, 57], [56, 56], [58, 54], [59, 53], [60, 52], [61, 51], [62, 50], [62, 48], [61, 49], [60, 50], [59, 51], [58, 52], [57, 53], [55, 55], [54, 56], [53, 57], [52, 58], [51, 59], [50, 60], [49, 61], [48, 62], [47, 63], [45, 63], [46, 62], [47, 61], [48, 60], [49, 59], [50, 58], [51, 57], [52, 56], [53, 55], [54, 54], [55, 53], [56, 52], [57, 51], [58, 50], [59, 49], [60, 48], [61, 47], [62, 46], [62, 44], [61, 45], [60, 46], [59, 47], [58, 48], [57, 49], [56, 50], [55, 51], [54, 52], [52, 54], [51, 55], [50, 56], [47, 59], [46, 60], [45, 61], [44, 62], [43, 63], [41, 63], [42, 62], [43, 61], [44, 60], [42, 60], [41, 61], [40, 62], [39, 63], [40, 60], [39, 61], [38, 62], [37, 63], [35, 63], [36, 62], [37, 61], [38, 60], [39, 59], [40, 58], [38, 58], [37, 59], [36, 60], [35, 61], [34, 62], [33, 63], [32, 62], [31, 63], [33, 61], [34, 60], [35, 59], [36, 58], [37, 57], [38, 56], [39, 55], [37, 55], [36, 56], [35, 57], [31, 61], [30, 62], [29, 63], [27, 63], [28, 62], [29, 61], [30, 60], [32, 58], [34, 56], [35, 55], [36, 54], [37, 53], [35, 53], [34, 54], [30, 58], [29, 59], [28, 60], [27, 61], [26, 62], [25, 63], [25, 61], [25, 59], [26, 60], [27, 59], [26, 58], [28, 58], [27, 57], [26, 56], [27, 55], [28, 56], [29, 57], [30, 56], [29, 55], [28, 54], [31, 55], [30, 54], [29, 53], [28, 52], [27, 51], [27, 49], [28, 50], [29, 51], [30, 52], [31, 53], [32, 54], [33, 53], [32, 52], [31, 51], [30, 50], [29, 49], [28, 48], [29, 47], [30, 48], [31, 49], [32, 50], [33, 51], [34, 52], [35, 51], [34, 50], [33, 49], [32, 48], [31, 47], [30, 46], [31, 45], [32, 46], [33, 47], [34, 48], [35, 49], [36, 50], [37, 49], [36, 48], [35, 47], [34, 46], [37, 47], [36, 46], [35, 45], [34, 44], [24, 58], [23, 59], [22, 60], [21, 61], [20, 62], [19, 63], [21, 63], [22, 62], [23, 61], [23, 63], [23, 57], [22, 58], [21, 59], [20, 60], [19, 61], [18, 62], [17, 63], [15, 63], [16, 62], [17, 61], [18, 60], [20, 58], [22, 56], [17, 59], [16, 60], [15, 61], [14, 62], [13, 63], [11, 63], [12, 62], [13, 61], [14, 60], [15, 59], [14, 58], [13, 59], [12, 60], [11, 61], [10, 62], [9, 63], [7, 63], [8, 62], [9, 61], [10, 60], [11, 59], [12, 58], [13, 57], [14, 56], [15, 55], [16, 54], [16, 52], [15, 53], [14, 54], [13, 55], [12, 56], [11, 57], [10, 58], [9, 59], [8, 60], [7, 61], [6, 62], [5, 63], [3, 63], [4, 62], [5, 61], [6, 60], [7, 59], [8, 58], [9, 57], [11, 55], [12, 54], [13, 53], [14, 52], [15, 51], [16, 50], [15, 49], [13, 51], [12, 52], [7, 57], [6, 58], [5, 59], [4, 60], [3, 61], [2, 62], [1, 63], [-1, 63], [0, 62], [1, 61], [2, 60], [3, 59], [4, 58], [5, 57], [6, 56], [7, 55], [12, 50], [-1, 61], [0, 60], [1, 59], [2, 58], [3, 57], [4, 56], [5, 55], [6, 54], [8, 50], [7, 51], [6, 52], [5, 53], [4, 54], [3, 55], [2, 56], [1, 57], [0, 58], [-1, 59], [-1, 57], [0, 56], [1, 55], [2, 54], [3, 53], [4, 52], [5, 51], [6, 50], [7, 49], [8, 48], [8, 46], [7, 47], [6, 48], [5, 49], [4, 50], [3, 51], [2, 52], [1, 53], [0, 54], [-1, 55], [-1, 53], [0, 52], [3, 49], [4, 48], [5, 47], [6, 46], [7, 45], [8, 44], [8, 42], [7, 43], [6, 44], [5, 45], [4, 46], [3, 47], [2, 48], [-1, 51], [-1, 49], [0, 48], [1, 47], [2, 46], [3, 45], [4, 44], [5, 43], [3, 43], [2, 44], [1, 45], [0, 46], [-1, 47], [-1, 45], [0, 44], [1, 43], [2, 42], [3, 41], [2, 40], [1, 41], [0, 42], [-1, 43], [-1, 41], [0, 40], [1, 39], [2, 38], [1, 37], [0, 38], [-1, 39], [-1, 37], [0, 36], [1, 35], [2, 34], [2, 32], [1, 33], [0, 34], [-1, 35], [-1, 33], [0, 32], [1, 31], [2, 30], [3, 29], [4, 28], [6, 26], [5, 25], [4, 26], [3, 27], [2, 28], [1, 29], [0, 30], [-1, 31], [-1, 29], [0, 28], [1, 27], [2, 26], [3, 25], [4, 24], [5, 23], [3, 23], [2, 24], [1, 25], [0, 26], [-1, 27], [-1, 25], [0, 24], [1, 23], [2, 20], [1, 21], [0, 22], [-1, 23], [-1, 21], [0, 20], [1, 19], [2, 18], [2, 16], [1, 17], [0, 18], [-1, 19], [-1, 17], [0, 16], [1, 15], [0, 14], [-1, 15], [1, 13], [3, 11], [5, 9], [7, 5], [6, 6], [4, 8], [3, 9], [2, 10], [1, 11], [0, 12], [-1, 13], [-1, 11], [0, 10], [2, 8], [1, 9], [3, 7], [4, 6], [6, 4], [6, 2], [5, 3], [4, 4], [3, 5], [2, 6], [1, 7], [0, 8], [-1, 9], [-1, 7], [0, 6], [1, 5], [2, 4], [3, 3], [4, 2], [5, 1], [6, 0], [5, -1], [4, 0], [3, 1], [2, 2], [1, 3], [0, 4], [-1, 5], [-1, 3], [0, 2], [1, 1], [2, 0], [3, -1], [1, -1], [0, 0], [-1, 1], [-1, -1], [11, -1], [11, 1], [12, 0], [13, -1], [15, -1], [14, 0], [13, 1], [12, 2], [13, 3], [14, 2], [15, 1], [16, 0], [17, -1], [19, -1], [18, 0], [17, 1], [16, 2], [15, 3], [14, 4], [13, 5], [13, 7], [14, 6], [15, 5], [16, 4], [17, 3], [18, 2], [19, 1], [20, 0], [21, -1], [23, -1], [22, 0], [21, 1], [20, 2], [19, 3], [18, 4], [17, 5], [16, 6], [15, 7], [15, 9], [16, 8], [18, 6], [17, 7], [19, 7], [18, 8], [17, 9], [16, 10], [17, 11], [18, 10], [19, 9], [21, 9], [20, 10], [19, 11], [18, 12], [17, 13], [18, 14], [19, 13], [20, 12], [21, 11], [22, 10], [22, 12], [21, 13], [20, 14], [19, 15], [19, 17], [20, 16], [21, 15], [22, 14], [23, 13], [23, 15], [22, 16], [21, 17], [20, 18], [19, 19], [20, 20], [21, 19], [22, 18], [23, 17], [21, 21], [20, 4], [21, 3], [22, 2], [23, 1], [24, 0], [25, -1], [27, -1], [26, 0], [25, 1], [24, 2], [23, 3], [22, 4], [21, 5], [23, 5], [24, 4], [26, 2], [25, 3], [27, 1], [28, 0], [29, -1], [31, -1], [30, 0], [29, 1], [28, 2], [27, 3], [25, 5], [23, 7], [27, 5], [29, 3], [30, 2], [31, 1], [32, 0], [33, -1], [35, -1], [34, 0], [33, 1], [32, 2], [29, 5], [31, 5], [34, 2], [35, 1], [36, 0], [37, -1], [39, -1], [38, 0], [37, 1], [33, 5], [32, 6], [31, 7], [30, 8], [29, 9], [32, 8], [34, 6], [37, 3], [39, 1], [40, 0], [41, -1], [43, -1], [42, 0], [40, 2], [38, 4], [37, 5], [36, 6], [33, 9], [32, 10], [32, 12], [33, 11], [34, 10], [37, 7], [36, 8], [39, 5], [41, 3], [42, 2], [44, 0], [45, -1], [47, -1], [46, 0], [45, 1], [43, 3], [42, 4], [41, 5], [39, 7], [38, 8], [37, 9], [35, 11], [38, 10], [39, 9], [41, 7], [43, 5], [44, 4], [48, 0], [49, -1], [51, -1], [50, 0], [49, 1], [45, 5], [44, 6], [42, 8], [40, 10], [39, 11], [42, 10], [43, 9], [44, 8], [46, 6], [45, 7], [48, 4], [49, 3], [51, 1], [52, 0], [53, -1], [55, -1], [54, 0], [53, 1], [52, 2], [51, 3], [50, 4], [49, 5], [48, 6], [48, 8], [49, 7], [52, 4], [53, 3], [54, 2], [55, 1], [56, 0], [57, -1], [59, -1], [58, 0], [57, 1], [56, 2], [55, 3], [54, 4], [53, 5], [51, 7], [50, 8], [49, 9], [52, 8], [53, 7], [55, 5], [56, 4], [57, 3], [58, 2], [59, 1], [60, 0], [61, -1], [62, 0], [61, 1], [60, 2], [59, 3], [58, 4], [57, 5], [56, 6], [55, 7], [54, 8], [53, 9], [53, 11], [56, 8], [57, 7], [58, 6], [59, 5], [60, 4], [61, 3], [62, 2], [62, 4], [61, 5], [60, 6], [58, 8], [55, 11], [55, 13], [56, 12], [57, 11], [58, 10], [59, 9], [60, 8], [61, 7], [62, 6], [62, 8], [61, 9], [60, 10], [59, 11], [62, 10], [61, 11], [60, 12], [59, 13], [62, 12], [61, 13], [60, 14], [59, 15], [58, 16], [62, 14], [61, 15], [60, 16], [59, 17], [60, 18], [61, 17], [62, 16], [62, 18], [61, 19], [60, 20], [59, 21], [58, 22], [57, 23], [58, 20], [58, 24], [59, 23], [60, 22], [61, 21], [62, 20], [62, 22], [61, 23], [60, 24], [59, 25], [58, 26], [57, 27], [56, 28], [57, 29], [58, 28], [59, 27], [60, 26], [61, 25], [62, 24], [62, 26], [61, 27], [60, 28], [59, 29], [58, 30], [58, 32], [59, 31], [60, 30], [61, 29], [62, 28], [55, 35], [51, 35], [53, 39], [54, 38], [55, 37], [58, 34], [59, 33], [60, 32], [61, 31], [62, 30], [62, 32], [61, 33], [60, 34], [59, 35], [57, 37], [56, 38], [55, 39], [54, 40], [53, 41], [54, 42], [55, 41], [56, 40], [57, 39], [58, 38], [59, 37], [60, 36], [61, 35], [62, 34], [62, 36], [61, 37], [60, 38], [59, 39], [58, 40], [57, 41], [56, 42], [55, 43], [56, 44], [57, 43], [58, 42], [59, 41], [60, 40], [61, 39], [62, 38], [55, 45], [50, 44], [51, 45], [52, 46], [51, 47], [52, 48], [47, 45], [48, 48], [45, 51], [45, 53], [46, 54], [55, 49], [56, 48], [57, 47], [58, 46], [59, 45], [60, 44], [61, 43], [62, 42], [52, 52], [51, 53], [51, 51]
]

for coord in water_coords:
    x, y = coord
    all_plates[x][y] = 1

for row in all_plates:
    print(row)
