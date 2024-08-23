#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include <jansson.h>

size_t WriteCallback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t total_size = size * nmemb;
    strcat(userp, (char *)contents);
    return total_size;
}
int main(void) {
    CURL *curl;
    CURLcode res;
    char buffer[100000] = "";
    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();
    if(curl) {
        struct curl_slist *headers = NULL;
        
        curl_easy_setopt(curl, CURLOPT_URL, "https://www.uu-proxy.com/api/free");
        
        headers = curl_slist_append(headers, "Accept: application/json, text/plain, */*");
        headers = curl_slist_append(headers, "Accept-Encoding: gzip, deflate, br, zstd");
        headers = curl_slist_append(headers, "Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,en-GB;q=0.6");
        headers = curl_slist_append(headers, "Connection: keep-alive");
        headers = curl_slist_append(headers, "Host: www.uu-proxy.com");
        headers = curl_slist_append(headers, "Referer: https://www.uu-proxy.com/");
        headers = curl_slist_append(headers, "Sec-Fetch-Dest: empty");
        headers = curl_slist_append(headers, "Sec-Fetch-Mode: cors");
        headers = curl_slist_append(headers, "Sec-Fetch-Site: same-origin");
        headers = curl_slist_append(headers, "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0");
        headers = curl_slist_append(headers, "sec-ch-ua: \"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"");
        headers = curl_slist_append(headers, "sec-ch-ua-mobile: ?0");
        headers = curl_slist_append(headers, "sec-ch-ua-platform: \"Windows\"");
        
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, buffer);
        
        res = curl_easy_perform(curl);
        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        } else {
            json_error_t error;
            json_t *root = json_loads(buffer, 0, &error);
            if(!root) {
                fprintf(stderr, "error: on line %d: %s\n", error.line, error.text);
            } else {
                json_t *free = json_object_get(root, "free");
                if(json_is_object(free)) {
                    json_t *proxies = json_object_get(free, "proxies");
                    if(json_is_array(proxies)) {
                        size_t index;
                        json_t *proxy;
                        json_array_foreach(proxies, index, proxy) {
                            const char *ip = json_string_value(json_object_get(proxy, "ip"));
                            const char *port = json_string_value(json_object_get(proxy, "port"));
                            const char *scheme = json_string_value(json_object_get(proxy, "scheme"));
                            printf("%s:%s:%s\n", ip, port, scheme);
                        }
                    }
                }
                json_decref(root);
            }
        }
        curl_slist_free_all(headers);
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();
    return 0;
}