// Swaps variables without the use of a temporary variable
// (Interview question at my dad's company...LOL), the XOR algorithm
template <typename T> void swap(T& a, T& b) {
    a ^= b;
    b ^= a;
    a ^= b;
}
