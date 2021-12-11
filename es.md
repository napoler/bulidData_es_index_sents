## ElasticSearch ClusterBlockException[blocked by: [FORBIDDEN/12/index read-only / allow delete (api)]

https://stackoverflow.com/questions/48155774/elasticsearch-read-only-allow-delete-auto-setting
执行接口
> curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'
>
> curl -XPUT -H "Content-Type: application/json" http://localhost:9200/tkit-index-test/_settings -d '{"index.blocks.read_only_allow_delete": null}'



```bash



curl -X PUT "http://127.0.0.1:9200/_cluster/settings?pretty" -H 'Content-Type: application/json' -d' { "transient": { "cluster.routing.allocation.disk.watermark.low": "50gb", "cluster.routing.allocation.disk.watermark.high": "20gb", "cluster.routing.allocation.disk.watermark.flood_stage": "10gb", "cluster.info.update.interval": "1m"}}'


curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_all/_settings -d '{"index.blocks.read_only_allow_delete": null}'
curl -XPUT -H "Content-Type: application/json" http://localhost:9200/_cluster/settings -d '{"transient": { "cluster.routing.allocation.disk.threshold_enabled": false }}'

```