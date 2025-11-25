/*
 Navicat Premium Dump SQL

 Source Server         : zane
 Source Server Type    : PostgreSQL
 Source Server Version : 180001 (180001)
 Source Host           : localhost:54321
 Source Catalog        : llmops
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 180001 (180001)
 File Encoding         : 65001

 Date: 25/11/2025 11:14:49
*/


-- ----------------------------
-- Table structure for app
-- ----------------------------
DROP TABLE IF EXISTS "public"."app";
CREATE TABLE "public"."app" (
  "id" uuid NOT NULL DEFAULT uuid_generate_v4(),
  "account_id" uuid NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "icon" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "description" text COLLATE "pg_catalog"."default" NOT NULL,
  "created_at" timestamptz(6) NOT NULL DEFAULT now(),
  "updated_at" timestamptz(6) NOT NULL DEFAULT now()
)
;
ALTER TABLE "public"."app" OWNER TO "postgres";

-- ----------------------------
-- Indexes structure for table app
-- ----------------------------
CREATE INDEX "idx_account_id" ON "public"."app" USING btree (
  "account_id" "pg_catalog"."uuid_ops" ASC NULLS LAST
);

-- ----------------------------
-- Uniques structure for table app
-- ----------------------------
ALTER TABLE "public"."app" ADD CONSTRAINT "app_name_key" UNIQUE ("name");

-- ----------------------------
-- Primary Key structure for table app
-- ----------------------------
ALTER TABLE "public"."app" ADD CONSTRAINT "app_pkey" PRIMARY KEY ("id");
