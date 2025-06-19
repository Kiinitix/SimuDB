#ifndef KV_STORE_HPP
#define KV_STORE_HPP

#include <string>
#include <unordered_map>
#include <tuple>

class KVStore {
public:
    void write(const std::string& key, const std::string& value, double timestamp);
    std::tuple<std::string, double> read(const std::string& key);
private:
    std::unordered_map<std::string, std::tuple<std::string, double>> store_;
};

#endif
