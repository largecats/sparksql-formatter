# https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL
class Keywords:
    RESERVED_KEYWORDS = [
        'ABORT',            # added in Hive 2.1.0
        'ADD',
        'ADMIN',
        'AFTER',
        'ANALYZE',
        'ARCHIVE',
        'ASC',
        'AUTOCOMMIT',       # added in Hive 2.0.0
        'BEFORE',
        'BUCKET',
        'BUCKETS',
        'CASCADE',
        'CHANGE',
        'CLUSTER',
        'CLUSTERED',
        'CLUSTERSTATUS',
        'COLLECTION',
        'COLUMNS',
        'COMMENT',
        'COMPACT',
        'COMPACTIONS',
        'COMPUTE',
        'CONCATENATE',
        'CONTINUE',
        'DATA',
        'DATABASES',
        'DATETIME',
        'DAY',
        'DAYS',             # added in Hive 2.2.0
        'DBPROPERTIES',
        'DEFERRED',
        'DEFINED',
        'DELIMITED',
        'DEPENDENCY',
        'DESC',
        'DETAIL',           # added in Hive 2.2.0
        'DIRECTORIES',
        'DIRECTORY',
        'DISABLE',
        'DISTRIBUTE',
        'DOW',              # added in Hive 2.2.0
        'ELEM_TYPE',
        'ENABLE',
        'ESCAPED',
        'EXCLUSIVE',
        'EXPLAIN',
        'EXPORT',
        'EXPRESSION',       # added in Hive 2.2.0
        'FIELDS',
        'FILE',
        'FILEFORMAT',
        'FIRST',
        'FORMAT',
        'FORMATTED',
        'FUNCTIONS',
        'HOLD_DDLTIME',
        'HOUR',
        'HOURS',            # added in Hive 2.2.0
        'IDXPROPERTIES',
        'IGNORE',
        'INDEX',
        'INDEXES',
        'INPATH',
        'INPUTDRIVER',
        'INPUTFORMAT',
        'ISOLATION',        # added in Hive 2.0.0
        'ITEMS',
        'JAR',
        'LEVEL',            # added in Hive 2.0.0
        'KEY',              # added in Hive 2.1.0
        'KEYS',
        'KEY_TYPE',
        'LAST',             # added in Hive 2.1.0
        'LIMIT',
        'LINES',
        'LOAD',
        'LOCATION',
        'LOCK',
        'LOCKS',
        'LOGICAL',
        'LONG',
        'MAPJOIN',
        'MATERIALIZED',
        'METADATA',
        'MINUS',
        'MINUTE',
        'MINUTES',          # added in Hive 2.2.0
        'MONTH',
        'MONTHS',           # added in Hive 2.2.0
        'MSCK',
        'NORELY',           # added in Hive 2.1.0
        'NOSCAN',
        'NOVALIDATE',       # added in Hive 2.1.0
        'NULLS',            # added in Hive 2.1.0
        'NO_DROP',
        'OFFLINE',
        'OPERATOR',         # added in Hive 2.2.0
        'OPTION',
        'OUTPUTDRIVER',
        'OUTPUTFORMAT',
        'OVERWRITE',
        'OWNER',
        'PARTITIONED',
        'PARTITIONS',
        'PLUS',
        'PRETTY',
        'PRINCIPALS',
        'PROTECTION',
        'PURGE',
        'QUARTER',          # added in Hive 2.2.0
        'READ',
        'READONLY',
        'REBUILD',
        'RECORDREADER',
        'RECORDWRITER',
        # 'REGEXP',           # removed in Hive 2.0.0
        'RELOAD',
        'RELY',             # added in Hive 2.1.0
        'RENAME',
        'REPAIR',
        'REPLACE',
        'REPLICATION',
        'RESTRICT',
        'REWRITE',
        # 'RLIKE',            # removed in Hive 2.0.0
        'ROLE',
        'ROLES',
        'SCHEMA',
        'SCHEMAS',
        'SECOND',
        'SECONDS',          # added in Hive 2.2.0
        'SEMI',
        'SERDE',
        'SERDEPROPERTIES',
        'SERVER',
        'SETS',
        'SHARED',
        'SHOW',
        'SHOW_DATABASE',
        'SKEWED',
        'SNAPSHOT',         # added in Hive 2.0.0
        'SORT',
        'SORTED',
        'SSL',
        'STATISTICS',
        'STORED',
        'STREAMTABLE',
        'STRING',
        'STRUCT',
        'SUMMARY',          # added in Hive 2.2.0
        'TABLES',
        'TBLPROPERTIES',
        'TEMPORARY',
        'TERMINATED',
        'TIMESTAMPTZ',      # added in Hive 3.0.0
        'TINYINT',
        'TOUCH',
        'TRANSACTION',      # added in Hive 2.0.0
        'TRANSACTIONS',
        'OFFSET',           # added in Hive 2.0.0
        'UNARCHIVE',
        'UNDO',
        'UNIONTYPE',
        'UNLOCK',
        'UNSET',
        'UNSIGNED',
        'URI',
        'USE',
        'UTC',
        'UTCTIMESTAMP',
        'VALIDATE',         # added in Hive 2.1.0
        'VALUE_TYPE',
        'VIEW',
        'VECTORIZATION',    # added in Hive 2.2.0
        'WEEK',             # added in Hive 2.2.0
        'WEEKS',            # added in Hive 2.0.0
        'WHILE',
        'WORK',             # added in Hive 2.0.0
        'WRITE',            # added in Hive 2.0.0
        'YEAR',
        'YEARS',            # added in Hive 2.2.0
        'ZONE'              # added in Hive 3.3.0
    ]

    NON_RESERVED_KEYWORDS = [
        'ALL',
        'ALTER',
        'AND',
        'ARRAY',
        'AS',
        'AUTHORIZATION',
        'BETWEEN',
        'BIGINT',
        'BINARY',
        'BOOLEAN',
        'BOTH',
        'BY',
        'CACHE',            # added in Hive 2.1.0
        'CASE',
        'CAST',
        'CHAR',
        'COLUMN',
        'COMMIT',           # added in Hive 2.0.0
        'CONF',
        'CONSTRAINT',       # added in Hive 2.1.0
        'CREATE',
        'CROSS',
        'CUBE',
        'CURRENT',
        'CURRENT_DATE',
        'CURRENT_TIMESTAMP',
        'CURSOR',
        'DATABASE',
        'DATE',
        'DAYOFWEEK',        # added in Hive 2.2.0
        'DECIMAL',
        'DELETE',
        'DESCRIBE',
        'DISTINCT',
        'DOUBLE',
        'DROP',
        'ELSE',
        'END',
        'EXCHANGE',
        'EXISTS',
        'EXTENDED',
        'EXTERNAL',
        'EXTRACT',          # added in Hive 2.2.0
        'FALSE',
        'FETCH',
        'FLOAT',
        'FLOOR',            # added in Hive 2.2.0
        'FOLLOWING',
        'FOR',
        'FOREIGN',          # added in Hive 2.1.0
        'FROM',
        'FULL',
        'FUNCTION',
        'GRANT',
        'GROUP',
        'GROUPING',
        'HAVING',
        'IF',
        'IMPORT',
        'IN',
        'INNER',
        'INSERT',
        'INT',
        'INTEGER',          # added in Hive 2.2.0
        'INTERSECT',
        'INTERVAL',
        'INTO',
        'IS',
        'JOIN',
        'LATERAL',
        'LEFT',
        'LESS',
        'LIKE',
        'LOCAL',
        'MACRO',
        'MAP',
        'MORE',
        'NONE',
        'NOT',
        'NULL',
        'NUMERIC',          # added in Hive 3.0.0
        'OF',
        'ON',
        'ONLY',             # added in Hive 2.0.0
        'OR',
        'ORDER',
        'OUT',
        'OUTER',
        'OVER',
        'PARTIALSCAN',
        'PARTITION',
        'PERCENT',
        'PRECEDING',
        'PRESERVE',
        'PRECISION',        # added in Hive 2.2.0
        'PRIMARY',          # added in Hive 2.1.0
        'PROCEDURE',
        'RANGE',
        'READS',
        'REDUCE',
        'REFERENCES',       # added in Hive 2.1.0
        'REGEXP',           # added in Hive 2.0.0
        'REVOKE',
        'RIGHT',
        'RLIKE',            # added in Hive 2.0.0
        'ROLLBACK',         # added in Hive 2.0.0
        'ROLLUP',
        'ROW',
        'ROWS',
        'SELECT',
        'SET',
        'SMALLINT',
        'START',            # added in Hive 2.0.0
        'SYNC',             # added in Hive 3.0.0
        'TABLE',
        'TABLESAMPLE',
        'THEN',
        'TIME',             # added in Hive 3.0.0
        'TIMESTAMP',
        'TO',
        'TRANSFORM',
        'TRIGGER',
        'TRUE',
        'TRUNCATE',
        'UNBOUNDED',
        'UNION',
        'UNIQUEJOIN',
        'UPDATE',
        'USER',
        'USING',
        'UTC_TMESTAMP',
        'VALUES',
        'VARCHAR',
        'VIEWS',            # added in Hive 2.2.0
        'WHEN',
        'WHERE',
        'WINDOW',
        'WITH'
    ]

    TOP_LEVEL_KEYWORDS = [
        'ADD',
        'AFTER',
        'ALTER COLUMN',
        'ALTER TABLE',
        'CROSS JOIN',
        'DELETE FROM',
        'EXCEPT',
        'FETCH FIRST',
        'FROM',
        'GROUP BY',
        'GO',
        'HAVING',
        'INNER JOIN',
        'INSERT INTO',
        'INSERT',
        'INTERSECT', 
        'INTERSECT ALL',
        'JOIN',
        'LEFT JOIN',
        'LEFT OUTER JOIN',
        'LIMIT',
        'MINUS',
        'MODIFY',
        'ORDER BY',
        'OUTER JOIN',
        'RIGHT JOIN',
        'RIGHT OUTER JOIN',
        'SELECT',
        'SET CURRENT SCHEMA',
        'SET SCHEMA',
        'SET',
        'UNION', 
        'UNION ALL',
        'UPDATE',
        'VALUES',
        'WHERE'
    ]

    TOP_LEVEL_KEYWORDS_NO_INDENT = [
        'CROSS JOIN',
        'JOIN',
        'LEFT JOIN',
        'LEFT OUTER JOIN',
        'INNER JOIN',
        'INTERSECT', 
        'INTERSECT ALL',
        'OUTER JOIN',
        'RIGHT JOIN',
        'RIGHT OUTER JOIN',
        'MINUS', 
        'UNION', 
        'UNION ALL'
    ]

    NEWLINE_KEYWORDS = [
        'AND',
        'CROSS APPLY',
        'CROSS JOIN',
        'ELSE',
        'INNER JOIN',
        'JOIN',
        'LEFT JOIN',
        'LEFT OUTER JOIN',
        'ON',
        'OR',
        'OUTER APPLY',
        'OUTER JOIN',
        'RIGHT JOIN',
        'RIGHT OUTER JOIN',
        'WHEN',
        'XOR'
    ]

# https://cwiki.apache.org/confluence/display/Hive/LanguageManual+UDF#LanguageManualUDF-MathematicalFunctions
class Functions:
    MATHEMATICAL_FUNCTIONS = [
        'round',
        'ceil',
        'ceiling',
        'rand',
        'exp',
        'ln',
        'log10',
        'log2',
        'log',
        'pow',
        'power',
        'sqrt',
        'bin',
        'hex',
        'unhdex',
        'conv',
        'abs',
        'pmod',
        'sin',
        'asin',
        'cos',
        'acos',
        'tan',
        'atan',
        'degrees',
        'radians',
        'positive',
        'negative',
        'sign',
        'e',
        'pi',
        'factorial',
        'cbrt',
        'shiftleft',
        'shiftright',
        'shiftrightunsigned',
        'greatest',
        'least',
        'width_bucket'
    ]
    
    COLLECTION_FUNCTIONS = [
        'size',
        'map_keys',
        'map_values',
        'array_contains',
        'sort_array'
    ]

    TYPE_CONVERSION_FUNCTIONS = [
        'binary',
        'cast'
    ]

    DATE_FUNCTIONS = [
        'from_unixtime',
        'unix_timestamp',
        'to_date',
        'year',
        'quarter',
        'month',
        'day',
        'hour',
        'minute',
        'second',
        'weekofyear',
        'extract',
        'datediff',
        'date_add',
        'date_sub',
        'from_utc_timestamp',
        'to_utc_timestamp',
        'current_date',
        'current_timestamp',
        'add_months',
        'last_day',
        'next_day',
        'trunc',
        'months_between',
        'date_format'
    ]

    CONDITIONAL_FUNCTIONS = [
        'if',
        'isnull',
        'isnotnull',
        'nvl',
        'COALESCE',
        'nullif',
        'assert_true'
    ]

    STRING_FUNCTIONS = [
        'ascii',
        'base64',
        'character_length',
        'chr',
        'concat',
        'context_ngrams',
        'concat_ws',
        'decode',
        'elt',
        'encode',
        'field',
        'find_in_set',
        'format_number',
        'get_json_object',
        'in_file',
        'instr',
        'length',
        'locate',
        'lower',
        'lpad',
        'ltrim',
        'ngrams',
        'octet_length',
        'parse_url',
        'printf',
        'quote',
        'regexp_extract',
        'regexp_replace',
        'repeat',
        'replace',
        'reverse',
        'rpad',
        'rtrim',
        'sentences',
        'space',
        'split',
        'str_to_map',
        'substr',
        'substring_index',
        'translate',
        'trim',
        'unbase64',
        'upper',
        'initcap',
        'levenhtein',
        'soundex'
    ]

    DATA_MASKING_FUNCTIONS = [
        'mask',
        'mask_first_n',
        'mask_last_n',
        'mask_show_first_n',
        'mask_show_last_n',
        'mask_hash'
    ]

    MISC_FUNCTIONS = [
        'java_method',
        'reflect',
        'hash',
        'current_user',
        'logged_in_user',
        'current_database',
        'md5',
        'sha1',
        'sha',
        'crc32',
        'sha2',
        'aes_decrypt',
        'version',
        'surrogate_key'
    ]

    AGGREGATE_FUNCTIONS = [
        'count',
        'sum',
        'avg',
        'min',
        'max',
        'variance',
        'var_samp',
        'stddev_pop',
        'stddev_samp',
        'covar_pop',
        'covar_samp',
        'corr',
        'percentile',
        'percentile_approx',
        'regr_avgx',
        'regr_avgy',
        'regr_count',
        'regr_intercept',
        'regr_r2',
        'regr_slope',
        'regr_sxx',
        'regr_sxy',
        'regr_syy',
        'histogram_numeric',
        'collect_set',
        'collect_list',
        'ntile'
    ]

    TABLE_GENERATING_FUNCTIONS = [
        'explode',
        'posexplode',
        'inline',
        'stack',
        'json_tuple',
        'parse_url_tuple'
    ]

    # https://cwiki.apache.org/confluence/display/Hive/LanguageManual+WindowingAndAnalytics#LanguageManualWindowingAndAnalytics-EnhancementstoHiveQL
    WINDOWING_FUNCTIONS = [
        'LEAD',
        'LAG',
        'FIRST_VALUE',
        'LAST_VALUE'
    ]

    ANALYTICS_FUNCTIONS = [
        'RANK',
        'ROW_NUMBER',
        'DENSE_RANK',
        'CUME_DIST',
        'PERCENT_RANK',
        'NTILE'
    ]

