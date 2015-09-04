// Swaps two numbers without the use of a temporary variable
// (Interview question at my dad's company...LOL), the XOR algorithm
template <typename T> void my_swap(T& a, T& b) {
    a ^= b;
    b ^= a;
    a ^= b;
}

