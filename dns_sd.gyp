{ 'targets': [
    { 'target_name': 'dns_sd'
    , 'sources': [ 'src/dns_sd.cpp'
                 , 'src/dns_service_browse.cpp'
                 , 'src/dns_service_enumerate_domains.cpp'
                 , 'src/dns_service_get_addr_info.cpp'
                 , 'src/dns_service_process_result.cpp'
                 , 'src/dns_service_ref.cpp'
                 , 'src/dns_service_ref_deallocate.cpp'
                 , 'src/dns_service_ref_sock_fd.cpp'
                 , 'src/dns_service_register.cpp'
                 , 'src/dns_service_resolve.cpp'
                 , 'src/mdns_utils.cpp'
                 , 'src/txt_record_ref.cpp'
                 , 'src/txt_record_create.cpp'
                 , 'src/txt_record_deallocate.cpp'
                 , 'src/txt_record_set_value.cpp'
                 , 'src/txt_record_get_length.cpp'
                 , 'src/txt_record_buffer_to_object.cpp'
                 ]
    , 'conditions': [
        [ 'OS!="mac" and OS!="win"', {
          'libraries': [ '-ldns_sd' ]
        }],
        ['OS=="win"', {
          'sources'     : [ 'src/winsock_watcher.cpp' ]
        , 'include_dirs': [ '$(BONJOUR_SDK_HOME)Include' ]
        , 'libraries'   : [ '-l$(BONJOUR_SDK_HOME)Lib/Win32/dnssd.lib'
                          , '-lws2_32.lib'
                          ]
        }],
      ]
    }
  ]
}

# vim: filetype=python shiftwidth=2 softtabstop=2 :
