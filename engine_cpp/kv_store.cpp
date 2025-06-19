#include "kv_store.hpp"

void KVStore::write(const std::string& key, const std::string& value, double timestamp) {
    store_[key] = std::make_tuple(value, timestamp);
}

std::tuple<std::string, double> KVStore::read(const std::string& key) {
    auto it = store_.find(key);
    if (it != store_.end()) {
        return it->second;
    }
    return std::make_tuple("", 0.0);
}
